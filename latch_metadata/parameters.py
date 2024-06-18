
from dataclasses import dataclass
import typing
import typing_extensions

from flytekit.core.annotation import FlyteAnnotation

from latch.types.metadata import NextflowParameter
from latch.types.file import LatchFile
from latch.types.directory import LatchDir, LatchOutputDir

# Import these into your `__init__.py` file:
#
# from .parameters import generated_parameters

generated_parameters = {
    'input': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title='Input/output options',
        description='Path to comma-separated file containing information about the samples in the experiment.',
    ),
    'id': NextflowParameter(
        type=typing.Optional[str],
        default='placement',
        section_title=None,
        description='Name of analysis',
    ),
    'alignmethod': NextflowParameter(
        type=typing.Optional[str],
        default='hmmer',
        section_title=None,
        description='Method used to align query sequences with.',
    ),
    'queryseqfile': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Fasta file with query sequences',
    ),
    'refseqfile': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='File with reference sequences. Any format supported by HMMER tools.',
    ),
    'hmmfile': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='HMM file. If provided, will be used to align both the reference and query sequences.',
    ),
    'refphylogeny': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Newick file with aligned reference sequences.',
    ),
    'model': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description="Evolutionary model to use for placement, e.g. 'LG'.",
    ),
    'taxonomy': NextflowParameter(
        type=typing.Optional[LatchFile],
        default=None,
        section_title=None,
        description='Tab-separated file with taxonomy assignments of reference sequences.',
    ),
    'outdir': NextflowParameter(
        type=typing_extensions.Annotated[LatchDir, FlyteAnnotation({'output': True})],
        default=None,
        section_title=None,
        description='The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.',
    ),
    'email': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='Email address for completion summary.',
    ),
    'multiqc_title': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title=None,
        description='MultiQC report title. Printed as page header, used for filename if not otherwise specified.',
    ),
    'multiqc_methods_description': NextflowParameter(
        type=typing.Optional[str],
        default=None,
        section_title='Generic options',
        description='Custom MultiQC yaml file containing HTML including a methods description.',
    ),
}

