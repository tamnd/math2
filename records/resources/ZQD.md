---
records:
    - id: ZQDCBNVGVV
      kind: course
      title: Matrix Analysis with Applications
      creators:
        - name: Sanjeev Kumar
          role: instructor
        - name: S. K. Gupta
          role: instructor
      ids:
        course: 00582g326:111107112
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Roorkee
              ids:
                nptel: "111107112"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111107112"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: ZQDX8E43SQ
      kind: preprint
      title: A Local Approach to Monogenity with an Application to Lenny Jones' Conjecture
      creators:
        - name: Michail Karatarakis
          role: author
        - name: Sumandeep Kaur
          role: author
      date: "2026-09-29"
      msc:
        - code: 11-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.NT
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-29"
          ids:
            arxiv: "2609.36811"
            zbl_id: "903188972"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.36811"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.36811"
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "903188972"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
