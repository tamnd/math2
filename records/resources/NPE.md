---
records:
    - id: NPEH1JWGNA
      kind: monograph
      title: Séminaire de Probabilités X Université de Strasbourg
      creators:
        - name: P. A. Meyer
          role: editor
      date: "1975"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 60-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1975"
          ids:
            doi:
                - 10.1007/bfb0101091
                - 10.1007/bfb0102980
            zbl: "0319.00007"
            zbl_id: "3499669"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540076810"
                    - "9783540381976"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1975"
              ids:
                isbn:
                    - "9783540071785"
                    - "9783540375180"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0101091
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0102980
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3499669"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.14 scope/1
          note: from in to in
    - id: NPEVE32HFP
      kind: preprint
      title: Critical oriented percolation enhanced along random supercritical horizontal lines
      creators:
        - name: Lucas Leproult
          role: author
        - name: Maria Eulália Vares
          role: author
      date: "2026-10-13"
      msc:
        - code: 60-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-13"
          ids:
            arxiv: "2610.18312"
            zbl_id: "903212692"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.18312"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.18312"
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "903212692"
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
