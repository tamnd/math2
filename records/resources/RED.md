---
records:
    - id: REDG6QVHM3
      kind: preprint
      title: Signed seeds and G-gradings on cluster algebras
      creators:
        - name: Lauren Williams
          role: author
        - name: Alan Yan
          role: author
      date: "2026-10-02"
      msc:
        - code: 05-XX
          from: arxiv
        - code: 16-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.CO
        - system: arxiv
          code: math.RA
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-02"
          ids:
            arxiv: "2610.03612"
            zbl_id: "903196158"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.03612"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.03612"
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "903196158"
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
    - id: REDMPX8TKR
      kind: monograph
      title: Arithmetic Theory of Elliptic Curves
      creators:
        - name: John H. Coates
          role: author
        - name: Kenneth A. Ribet
          role: author
        - name: Ralph Greenberg
          role: author
        - name: Karl Rubin
          role: author
        - name: Carlo Viola
          role: editor
      date: "1999"
      msc:
        - code: 11-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          date: "1999"
          ids:
            doi: 10.1007/bfb0093451
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1999"
              ids:
                isbn:
                    - "9783540665465"
                    - "9783540481607"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0093451
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
