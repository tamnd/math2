---
records:
    - id: KGB9VXFYW1
      kind: monograph
      title: Potential Theory
      creators:
        - name: Lester L. Helms
          role: author
      date: "2009"
      msc:
        - code: 31-01
          from: zbmath_search
        - code: 35J25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2009"
          ids:
            doi:
                - 10.1007/978-1-4471-6422-7
                - 10.1007/978-1-84882-319-8
            zbl: "1180.31001"
            zbl_id: "5528183"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2014"
              ids:
                isbn:
                    - "9781447164210"
                    - "9781447164227"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer London
              date: "2009"
              ids:
                isbn:
                    - "9781848823181"
                    - "9781848823198"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-6422-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-84882-319-8
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "5528183"
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
    - id: KGBKNQB52Z
      kind: preprint
      title: A pseudospectral quadrature method for Navier-Stokes equations on rotating spheres
      creators:
        - name: M. Ganesh
          role: author
        - name: Q. T. Le Gia
          role: author
        - name: I. H. Sloan
          role: author
      date: "2010-09-17"
      msc:
        - code: 65-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.NA
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2010-09-17"
          ids:
            arxiv: "1009.3308"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "1009.3308"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "1009.3308"
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
