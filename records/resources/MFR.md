---
records:
    - id: MFR6JV5AKP
      kind: monograph
      title: Second Year Calculus
      creators:
        - name: David M. Bressoud
          role: author
      date: "1991"
      msc:
        - code: 26-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1991"
          ids:
            doi: 10.1007/978-1-4612-0959-1
            zbl: "0729.26003"
            zbl_id: "51134"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1991"
              ids:
                isbn:
                    - "9780387976068"
                    - "9781461209591"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0959-1
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "51134"
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
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: MFR807V4YG
      kind: preprint
      title: Instantaneous Exponential Ill-posedness of the BGK Model in a Half-Space with Inflow Boundary Conditions
      creators:
        - name: Donghyun Lee
          role: author
        - name: Sungbin Park
          role: author
        - name: Sung-jun Son
          role: author
        - name: Seok-Bae Yun
          role: author
      date: "2026-10-01"
      msc:
        - code: 35-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.AP
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-10-01"
          ids:
            arxiv: "2610.01225"
            zbl_id: "903193771"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.01225"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2610.01225"
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "903193771"
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
